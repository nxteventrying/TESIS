import matplotlib.pyplot as plt

def model_assessment_comparison(train,test,predictions_ensemble, chart_title):
  plt.figure(figsize = (10,4))
  plt.plot(train, color = 'blue',label = 'train')
  plt.plot(test, color = 'orange', marker='*',label = 'test')


  colors = ['lime', 'black', 'purple','red','gray']

  for i, (key, value) in enumerate(predictions_ensemble.items()):
    plt.plot(value, label=key, color=colors[i % len(colors)])

  plt.title(chart_title)
  plt.legend()
  plt.show()