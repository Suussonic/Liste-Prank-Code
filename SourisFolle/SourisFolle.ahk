SetTimer(MoveMouse, 50)

MoveMouse() {
    offsetX := Random(-100, 100)
    offsetY := Random(-100, 100)
    MouseMove(offsetX, offsetY, 0, "R")
}
