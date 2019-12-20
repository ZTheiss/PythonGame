




class Enemy(object){
    walkrightMovementEnemy = [pygame.image.load('EnemySprits/R1E.png'), pygame.image.load('EnemySprits/R2E.png'), pygame.image.load('EnemySprits/R3E.png'), 
    pygame.image.load('EnemySprits/R4E.png'), pygame.image.load('EnemySprits/R5E.png'),pygame.image.load('EnemySprits/R4E.png'), 
    pygame.image.load('EnemySprits/R6E.png'),pygame.image.load('EnemySprits/R7E.png'), pygame.image.load('EnemySprits/R8E.png'),
    pygame.image.load('EnemySprits/R9E.png'),pygame.image.load('EnemySprits/R10E.png'), pygame.image.load('EnemySprits/R11E.png')]

    walkleftMovementEnemy = [pygame.image.load('EnemySprits/L1E.png'), pygame.image.load('EnemySprits/L2E.png'), pygame.image.load('EnemySprits/L3E.png'), 
    pygame.image.load('EnemySprits/L4E.png'), pygame.image.load('EnemySprits/L5E.png'),pygame.image.load('EnemySprits/L4E.png'), 
    pygame.image.load('EnemySprits/L6E.png'),pygame.image.load('EnemySprits/L7E.png'), pygame.image.load('EnemySprits/L8E.png'),
    pygame.image.load('EnemySprits/L9E.png'),pygame.image.load('EnemySprits/L10E.png'), pygame.image.load('EnemySprits/L11E.png')]
    def __init__(self, xlocation, ylocation, widthEnemy, heightEnemy, end):
        self.xlocation = xlocation #Left Right
        self.ylocation = ylocation #Up Down
        self.widthEnemy = widthEnemy
        self.heightEnemy = heightEnemy
        self.end = end
        self.walkCount = 0
        self.vel = 3

    def draw(self, wind):
        pass

    def move(self):
        pass
}