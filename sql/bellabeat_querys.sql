--TASK 1. Comprehensive Descriptive Analysis of Physical Activity.
select
avg(totaldistance) filter (where totaldistance != 0) as promedio_distancia_total,
	min(totaldistance) as distancia_total_minima,
	max(totaldistance) as distancia_total_maxima,
	avg(totalsteps) filter (where totalsteps != 0) as promedio_pasos_total,
	min(totalsteps) as pasos_total_minima,
	max(totalsteps) as pasos_total_maxima,
	avg(calories) filter (where calories != 0) as promedio_calorias,
	min(calories) as calorias_minima,
	max(calories) as calorias_maxima,
	avg(sedentaryminutes) filter (where sedentaryminutes != 0) as promedio_sedentario,
	min(sedentaryminutes) as sedentario_minimo,
	max(sedentaryminutes) as sedentario_maximo
from dailyactivity d;


--TASK 2. User Segmentation by Physical Activity Level.
-- Step 1: Create a virtual table and call it "clasificacion_usuarios"
WITH clasificacion_usuarios AS (
   select
		id,
		round(avg(steptotal) filter (where steptotal != 0),0) as promedio_pasos,
		case
			when round(avg(steptotal) filter (where steptotal != 0),0) < 5000 then 'sedentario'
			when round(avg(steptotal) filter (where steptotal != 0),0) between 5000 and 7499 then 'ligeramente activo'
			when round(avg(steptotal) filter (where steptotal != 0),0) between 7500 and 9999 then 'activo'
			else 'altamanente activo'	
		end as categoria_actividad
	from
		dailysteps
	group by
		id
	order by
		id asc
	)
-- Step 2: Use the virtual table for doing the final count.
SELECT
   categoria_actividad,
   COUNT(*) AS total_usuarios
FROM clasificacion_usuarios
GROUP BY categoria_actividad
ORDER BY total_usuarios DESC;


--TASK 3. Analysis of Temporal Trends.
select
	extract(isodow from activitydate) as numero_dia,
	to_char (activitydate,'Day') as nombre_dia,
	round(avg(totalsteps) filter (where totalsteps != 0),0) as promedio_pasos,
	round(avg(calories),0) as promedio_calorias,
	round(avg(sedentaryminutes) filter (where sedentaryminutes != 0),0) as promedio_minutos_sedentarios
from
	dailyactivity
group by
	extract(isodow from activitydate),
	to_char (activitydate,'Day')
order by
	numero_dia asc;


--TASK 4. Analysis of Physical Intensity by Time Slot (Shifts)
-- Step 1: Create virtual table called "clasificacion_turnos"
with clasificacion_turnos as (
  select
		extract(hour from activityhour) as hora,
		case
			when extract(hour from activityhour) between 0 and 5 then 'Madrugada'
			when extract(hour from activityhour) between 6 and 11 then 'Mañana'
			when extract(hour from activityhour) between 12 and 17 then 'Tarde'
			else 'Noche'	
		end as turno,
		steptotal
	from
		hourlysteps
	)

  -- Step 2: Let's use the virtual table to calculate the averages.
select
  turno,
  round(avg(steptotal),0) as promedio_pasos
from clasificacion_turnos
group by turno
order by promedio_pasos desc;

