 # --- Create blocks


    for row in range(1):
        
        for column in range(0, blockcount):
            
            block = Block(purple, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        
        top += block_height + 2

    for row in range(1):
        
        for column in range(0, blockcount):
            
            block = Block(blue, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        
        top += block_height + 2

    for row in range(1):
        
        for column in range(0, blockcount):
            
            block = Block(lime, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        
        top += block_height + 2

    for row in range(1):
        
        for column in range(0, blockcount):
            
            block = Block([255,255,0], column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        
        top += block_height + 2

    for row in range(1):
        
        for column in range(0, blockcount):
            
            block = Block(red, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        
        top += block_height + 2
