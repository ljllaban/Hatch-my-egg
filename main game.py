    # Is the game over?
    game_over = False


    # Exit the program?
    exit_program = False

    # Main program loop
    while exit_program != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 exit_program=True
                 play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            exit_program=True
                    #__init__()
        # Limit to 30 fps
        clock.tick(30)

        # Clear the screen
        screen.fill(black)
        
        # Process the events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True
        
        # Update the ball and player position as long
        # as the game is not over.
        if not game_over:
            # Update the player and ball positions
            player.update()
            game_over = ball.update()
           

        # If we are done, print game over
        if game_over:
            text = font.render("Game Over ! Click to Restart ", True, white)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 300
            screen.blit(text, textpos)
           
        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player, balls, False):
            # The 'diff' lets you try to bounce the ball left or right 
            # depending where on the paddle you hit it
            diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
            
            # Set the ball's y position in case 
            # we hit the ball on the edge of the paddle
            ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
            ball.bounce(diff)
        
        # Check for collisions between the ball and the blocks
        deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
        
        # If we actually hit a block, bounce the ball
        if len(deadblocks) > 0:
            ball.bounce(0)
            
            # Game ends if all the blocks are gone
            if len(blocks) == 0:
                game_over = True
        
        # Draw Everything
        allsprites.draw(screen)

        # Flip the screen and show what we've drawn
        pygame.display.flip()
#pygame.quit()
