import pygame

class Ship():
    def __init__(self,screen):
        """初始化ship并设置其初始位置"""
        self.screen = screen
        
        self.image = pygame.image.load('images/ship.bmp') #加载ship图片
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)


