blog_1 = 'Ivanova is G'
blog_2 = 'Buffy4Ever'
blog_3 = 'lost in time and space'


def blog_posts(title, *args):
    print('title: {}'.format(title))
    for blog in args:
        print(blog)


blog_posts(blog_1)
blog_posts(blog_1, blog_2)
blog_posts(blog_1, blog_2, blog_3)

# with names
site_title = 'Best Blogs'


def best_blog(title, **kwargs):
    print(title)
    for b_title, post in kwargs.items():
        print(b_title, post)


best_blog(
    site_title,
    blog_1='Ivanova is G',
    blog_2='Buffy4Ever',
    blog_3='lost and found in space')


# *args and **kwargs
def best_blogs(title, *args, **kwargs):
    print(title)
    for arg in args:
        print(arg)
    for b_title, post in kwargs.items():
        print(b_title, post)


best_blogs(
    site_title,
    '1',
    '3',
    '4',
    '5',
    blog_1='Ivanova is G',
    blog_2='Buffy4Ever',
    blog_3='lost and found in space')

import matplotlib.pyplot as plt 

def graph_operation(x,y):
    print('x={},y={}'.format(x,y))
    plt.plot(x,y)
    plt.show()

x1 = [1,2,3]
y1 = [4,5,6]

graph_operation(x1,y1)

graph_me = [x1,y1]

graph_operation(*graph_me)