class GeometryApp:
    def main(args):
        import circle, rectangle, triangle
        circle = circle.Circle(5.0)
        print(f"Площадь круга: {circle.getArea()}")
        print(f"Периметр круга: {circle.getPerimeter()}")

        rectangle = rectangle.Rectangle(4.0, 6.0)
        print(f"Площадь прямоугольника: {rectangle.getArea()}")
        print(f"Периметр прямоугольника: {rectangle.getPerimeter()}")

        triangle = triangle.Triangle(3.0, 4.0, 5.0)
        print(f"Площадь треугольника: {triangle.getArea()}")
        print(f"Периметр треугольника: {triangle.getPerimeter()}")

GeometryApp.main(GeometryApp)