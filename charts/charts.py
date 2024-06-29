import matplotlib.pyplot as plt

# def generate_pie_chart(labels, values):
def generate_pie_chart():
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]

  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('pie.png')
  plt.show()