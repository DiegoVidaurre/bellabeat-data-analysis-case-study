#

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
