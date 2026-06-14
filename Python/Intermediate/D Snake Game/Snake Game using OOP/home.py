def snake_game():
    import screen
    import snake
    import food
    import time
    import score
    import random
    scrn=screen.Display()
    snake_organ=snake.SnakeBody()
    snake_food=food.Food()
    score_board=score.SnakeScore()
    def up():
        snake_organ.up()
    def down():
        snake_organ.down()
    def left():
        snake_organ.left()
    def right():
        snake_organ.right()
    def grow():
        snake_organ.grow()
    scrn.disp.listen()
    scrn.disp.onkeypress(up,"Up")
    scrn.disp.onkeypress(down,"Down")
    scrn.disp.onkeypress(left,"Left")
    scrn.disp.onkeypress(right,"Right")
    scrn.disp.onkeypress(snake_game,"z")
    game="on"
    while game=="on":
        scrn.update()
        time.sleep(0.1)
        if -300 < snake_organ.snake_organ_list[0].xcor() < 300 and -300 < snake_organ.snake_organ_list[0].ycor() < 300:
            snake_organ.move()
            snake_organ.rainbow("live")
        else:
            scrn.create_border("red")
            scrn.disp.bgcolor(1.0, 0.3843137254901961, 0.26666666666666666)
            scrn.disp.tracer(1)
            game="off"

        if snake_food.apple.xcor() - 20 < snake_organ.snake_organ_list[0].xcor() < snake_food.apple.xcor() + 20 and snake_food.apple.ycor() - 20 < snake_organ.snake_organ_list[0].ycor() < snake_food.apple.ycor() + 20:
            grow()
            score_board.score+=1
            score_board.score_agent.clear()
            score_board.score_display()
            snake_food.gen_food()

        for part in snake_organ.snake_organ_list:
            if part.xcor()-20<snake_organ.snake_organ_list[0].xcor()<part.xcor()+20 and part.ycor()-20<snake_organ.snake_organ_list[0].ycor()<part.ycor()+20 and part!=snake_organ.snake_organ_list[0]:
                snake_organ.rainbow("dead")
                scrn.disp.tracer(1)
                game="off"

    scrn.close()
snake_game()