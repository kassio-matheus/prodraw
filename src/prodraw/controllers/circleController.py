from prodraw.models.circle import Circle
from prodraw.views.circleView import circleView


class CircleController:

    obj = {'obj':None}
    
    @staticmethod
    def start(bg):
        circle = Circle(bg=bg)
        def start_circle(event):
            circle.start(event)

        CircleController.obj['obj'] = circle
        return start_circle
    
    @staticmethod
    def update(view: circleView):
        circle = CircleController.obj['obj']

        def update_circle(event):
            circle.update(event)
            if circle.empty():
                view.draw(circle)

        return update_circle
    
    @staticmethod
    def add(view : circleView,figures):
        circle = CircleController.obj['obj']

        def add_circle(event):

            view.draw_all(figures)
            circle.add(figures)

        return add_circle

    @staticmethod
    def delete(view: circleView):
        view.delete()

