import pandas as pd

# TASK 1. Comprehensive Descriptive Analysis of Physical Activity.

resumen = pd.DataFrame({
   'promedio_distancia_total': [dailyactivity.loc[dailyactivity['totaldistance'] != 0, 'totaldistance'].mean()],
   'distancia_total_minima': [dailyactivity['totaldistance'].min()],
   'distancia_total_maxima': [dailyactivity['totaldistance'].max()],
  
   'promedio_pasos_total': [dailyactivity.loc[dailyactivity['totalsteps'] != 0, 'totalsteps'].mean()],
   'pasos_total_minima': [dailyactivity['totalsteps'].min()],
   'pasos_total_maxima': [dailyactivity['totalsteps'].max()],
  
   'promedio_calorias': [dailyactivity.loc[dailyactivity['calories'] != 0, 'calories'].mean()],
   'calorias_minima': [dailyactivity['calories'].min()],
   'calorias_maxima': [dailyactivity['calories'].max()],
  
   'promedio_sedentario': [dailyactivity.loc[dailyactivity['sedentaryminutes'] != 0, 'sedentaryminutes'].mean()],
   'sedentario_minimo': [dailyactivity['sedentaryminutes'].min()],
   'sedentario_maximo': [dailyactivity['sedentaryminutes'].max()]
})


print(resumen)


# TASK 2. User Segmentation by Physical Activity Level.
# Step 1: Calculate the average number of steps per ID (filtering out zeros) and round the result.

pasos_filtrados = (
   dailysteps[dailysteps['steptotal'] != 0]
   .groupby('id')['steptotal']
   .mean()
   .round(0)
   .reset_index(name='promedio_pasos')
)

#Step 2: Creating conditions and categories
condiciones = [
   pasos_filtrados['promedio_pasos'] < 5000,
   pasos_filtrados['promedio_pasos'].between(5000, 7499),
   pasos_filtrados['promedio_pasos'].between(7500, 9999),
]
categorias = ['sedentario', 'ligeramente activo', 'activo']

# If none of the above conditions are met, assign 'altamente_activo' (ELSE)

pasos_filtrados['categoria_actividad'] = np.select(
   condiciones, categorias, default='altamente activo')

# Step 3: Group the results by category and activity, and perform the final count.
resultado = (
   pasos_filtrados.groupby('categoria_actividad', as_index=False)
   .size()
   .rename(columns={'size': 'total_usuarios'})
   .sort_values(by='total_usuarios', ascending=False)
   .reset_index(drop=True)
)
print(resultado)


#TASK 3. Analysis of Temporal Trends.

dailyactivity['activitydate'] = pd.to_datetime(dailyactivity['activitydate'])
dailyactivity['numero_dia'] = dailyactivity['activitydate'].dt.dayofweek + 1
dailyactivity['nombre_dia'] = dailyactivity['activitydate'].dt.day_name()
resultado = (
    dailyactivity.groupby(['numero_dia', 'nombre_dia'], as_index=False)
    .agg(
        promedio_pasos=(
            'totalsteps',
            lambda x: round(x[x != 0].mean(), 0) if (x != 0).any() else 0
        ),
        promedio_calorias=('calories', lambda x: round(x.mean(), 0)),
        promedio_minutos_sedentarios=(
            'sedentaryminutes',
            lambda x: round(x[x != 0].mean(), 0) if (x != 0).any() else 0
        ),
    )
    .sort_values(by='numero_dia', ascending=True)
    .reset_index(drop=True)
)

print(resultado)


#TASK 4. Analysis of Physical Intensity by Time Slot (Shifts)
hourlysteps['activityhour'] = pd.to_datetime(hourlysteps['activityhour'])
horas = hourlysteps['activityhour'].dt.hour
condiciones = [
   horas.between(0, 5),
   horas.between(6, 11),
   horas.between(12, 17),
]
turnos = ['Madrugada', 'Mañana', 'Tarde']
hourlysteps['turno'] = np.select(condiciones, turnos, default='Noche')
resultado = (
   hourlysteps.groupby('turno', as_index=False)['steptotal']
   .mean()
   .round(0)
   .rename(columns={'steptotal': 'promedio_pasos'})
   .sort_values(by='promedio_pasos', ascending=False)
   .reset_index(drop=True)
)
print(resultado)
