import matplotlib.pyplot as mpt

subjects = ["Maths","English","Hindi","Physics"]
percentage = [60,15,10,25]
gap = [0.05,0.05,0.09,0.09]
color = ["red","green","blue","yellow"]

mpt.pie(
    percentage,
    labels = subjects,
    explode=gap,
    shadow=True,
    startangle=90,
    wedgeprops={'edgecolor': 'black','linewidth': 2}
)

mpt.show()