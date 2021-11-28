import pygame
from random import choice
from sprites.bottom import Bottom
from sprites.backround import Board
from sprites.piece_creator import creator
from sprites.piece_rotator import rotator
from sprites.block import Block


SHAPES = [
    "SHAPE_I",
    "SHAPE_L",
    "SHAPE_T",
    "SHAPE_SQ"
]

class GameState:
    def __init__(self):
        self.pick_next()
        self.all_sprites = pygame.sprite.Group()
        # self.bottom = pygame.sprite.Group()
        self.one_piece = Block(20, 300)
        print(self.one_piece.rect.left)
        self.pieces = creator(self.next_piece, 540, 10)
        # self.pieces.add(self.one_piece)
        self.fallen = pygame.sprite.Group()
        self.backround = Board(0, 0)
        self.bottom = pygame.sprite.Group()
        self.bottom.add(Bottom())
        # self.piece_L = pygame.sprite.Group()
        # self.piece_L.add(Block(375, 10))
        # self.piece_L.add(Block(405, 10))
        # self.piece_L.add(Block(405, 40))
        # self.piece_L.add(Block(405, 70))
        # self.pieces.add(self.piece_L)

        self.all_sprites.add(self.backround, self.bottom, self.pieces, self.fallen)
        print(self.all_sprites)

    def move(self, x_coord=0, y_coord=0):
        for piece in self.pieces:
            piece.rect.move_ip(x_coord, y_coord)

    def rotate(self):
        x,y = 10000,10000
        count = 0
        type = ""
        dir = ""
        for piece in self.pieces:
            if piece.rect.x < x:
                x =  piece.rect.x
            if piece.rect.y < y:
                y = piece.rect.y
            count += 1
            type = piece.type
            dir = piece.orientation
        new = rotator(self.next_piece, x , y , dir)
        self.pieces.empty()
        self.pieces.add(new)
        self.all_sprites.add(self.pieces)

        self.pieces = new
        self.all_sprites.add(self.pieces)

    def check_for_collision(self):          

        if pygame.sprite.groupcollide(self.pieces,self.fallen, False, False):
            self.move(x_coord=0, y_coord=-32)
            self.fallen.add(self.pieces)
            #self.pieces.remove()         
            self.spawn_new_piece()
            return True
                                
        elif pygame.sprite.groupcollide(self.pieces,self.bottom, False, False):
            #self.move(x_coord=0, y_coord=-32)
            self.fallen.add(self.pieces)
            #self.pieces.remove()

            self.spawn_new_piece()
            return True
        return False
                    
    def spawn_new_piece(self):
        self.pick_next()
        self.pieces = creator(self.next_piece, 540, 10)
        self.all_sprites.add(self.pieces)

    def pick_next(self):
        self.next_piece = choice(SHAPES)
    # def make_like_a_snake():
        # This will make the piece move like a snake
        # if we for some reason need it
        #
        # prev_x,prev_y = None, None
        # for piece in self.pieces:
        #     if not prev_x:
        #         prev_x = piece.rect.x
        #         prev_y = piece.rect.y
        #         piece.rect.move_ip(x,y)
        #     else:
        #         a,b = piece.rect.x, piece.rect.y
        #         piece.rect.move_ip(prev_x-a,prev_y-b)
        #         prev_x, prev_y = a,b
