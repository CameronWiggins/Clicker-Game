import pygame, sys

wire_img=pygame.image.load("wire.png")
wire_img=pygame.transform.scale(wire_img, (240,140))

mouse_img=pygame.image.load("mouse.png")
mouse_img=pygame.transform.scale(mouse_img, (150,200))

class Game:
  def __init__(self):
    self.wireImg = wire_img
    self.wire = self.wireImg.get_rect()
    self.wire.center=(318,203)

    self.img = mouse_img
    self.mouse=self.img.get_rect()
    self.mouse.center=(400,370)

    self.time = 0
    self.points = 0
    self.point_per_click = 1
    self.clicked = False

    self.upgradeBtn1 = pygame.Rect(5, 50, 195, 87)
    self.upgrade1_cost = 10
    self.upgradeBtn2 = pygame.Rect(5, 152, 195, 87)
    self.upgrade2_cost = 70
    self.upgradeBtn3 = pygame.Rect(5, 254, 195, 87)
    self.upgrade3_cost = 600
    self.upgradeBtn4 = pygame.Rect(5, 356, 195, 87)
    self.upgrade4_cost = 3000
    self.upgradeBtn5 = pygame.Rect(5, 458, 195, 87)
    self.upgrade5_cost = 20000
    self.upgradeBtn6 = pygame.Rect(600, 50, 195, 87)
    self.upgrade6_cost = 250
    self.autoMulti_1 = 0
    self.upgradeBtn7 = pygame.Rect(600, 152, 195, 87)
    self.upgrade7_cost = 550
    self.autoMulti_2 = 0
    self.upgradeBtn8 = pygame.Rect(600, 254, 195, 87)
    self.upgrade8_cost = 900
    self.autoMulti_3 = 0
    self.upgradeBtn9 = pygame.Rect(600, 356, 195, 87)
    self.upgrade9_cost = 1300
    self.autoMulti_4 = 0
    self.upgradeBtn10 = pygame.Rect(600, 458, 195, 87)
    self.upgrade10_cost = 1800
    self.autoMulti_5 = 0

  def upgrade(self):
    self.edu_label_1_1 = edu_font.render("Research", True, "#ffffff")
    self.edu_label_1_2 = edu_font.render("Cybersecurity Trends", True, "#ffffff")
    self.upgrade1_description = description_font.render(f"(+1 point per click)", True, "#ffffff")
    self.display1_cost = cost_font.render(f"Cost: {str(self.upgrade1_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn1, border_radius=15)
    screen.blit(self.edu_label_1_1, (15,58))
    screen.blit(self.edu_label_1_2, (15,75))
    screen.blit(self.upgrade1_description, (15,92))
    screen.blit(self.display1_cost, (15,110))

    self.edu_label_2_1 = edu_font.render("Secure", True, "#ffffff")
    self.edu_label_2_2 = edu_font.render("Backups", True, "#ffffff")
    self.upgrade2_description = description_font.render(f"(+5 points per click)", True, "#ffffff")
    self.display2_cost = cost_font.render(f"Cost: {str(self.upgrade2_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn2, border_radius=15)
    screen.blit(self.edu_label_2_1, (15,160))
    screen.blit(self.edu_label_2_2, (15,177))
    screen.blit(self.upgrade2_description, (15,194))
    screen.blit(self.display2_cost, (15,212))

    self.edu_label_3_1 = edu_font.render("Virus", True, "#ffffff")
    self.edu_label_3_2 = edu_font.render("Scan", True, "#ffffff")
    self.upgrade3_description = description_font.render(f"(+25 points per click)", True, "#ffffff")
    self.display3_cost = cost_font.render(f"Cost: {str(self.upgrade3_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn3, border_radius=15)
    screen.blit(self.edu_label_3_1, (15,262))
    screen.blit(self.edu_label_3_2, (15,279))
    screen.blit(self.upgrade3_description, (15,296))
    screen.blit(self.display3_cost, (15,314))

    self.edu_label_4_1 = edu_font.render("Social Engineering", True, "#ffffff")
    self.edu_label_4_2 = edu_font.render("Training", True, "#ffffff")
    self.upgrade4_description = description_font.render(f"(x2 points per click)", True, "#ffffff")
    self.display4_cost = cost_font.render(f"Cost: {str(self.upgrade4_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn4, border_radius=15)
    screen.blit(self.edu_label_4_1, (15,364))
    screen.blit(self.edu_label_4_2, (15,381))
    screen.blit(self.upgrade4_description, (15,398))
    screen.blit(self.display4_cost, (15,416))

    self.edu_label_5_1 = edu_font.render("Update", True, "#ffffff")
    self.edu_label_5_2 = edu_font.render("Hardware", True, "#ffffff")
    self.upgrade5_description = description_font.render(f"(x5 points per click)", True, "#ffffff")
    self.display5_cost = cost_font.render(f"Cost: {str(self.upgrade5_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn5, border_radius=15)
    screen.blit(self.edu_label_5_1, (15,466))
    screen.blit(self.edu_label_5_2, (15,483))
    screen.blit(self.upgrade5_description, (15,500))
    screen.blit(self.display5_cost, (15,518))

    self.edu_label_6_1 = edu_font.render("Hire Members", True, "#ffffff")
    self.edu_label_6_2 = edu_font.render("to Cyber Team", True, "#ffffff")
    self.upgrade6_description = description_font.render(f"(+1 points per ten seconds)", True, "#ffffff")
    self.display6_cost = cost_font.render(f"Cost: {str(self.upgrade6_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn6, border_radius=15)
    screen.blit(self.edu_label_6_1, (610,58))
    screen.blit(self.edu_label_6_2, (610,75))
    screen.blit(self.upgrade6_description, (610,92))
    screen.blit(self.display6_cost, (610,110))

    self.edu_label_7_1 = edu_font.render("Routine", True, "#ffffff")
    self.edu_label_7_2 = edu_font.render("Password Change", True, "#ffffff")
    self.upgrade7_description = description_font.render(f"(+10 points per half a minute)", True, "#ffffff")
    self.display7_cost = cost_font.render(f"Cost: {str(self.upgrade7_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn7, border_radius=15)
    screen.blit(self.edu_label_7_1, (610,160))
    screen.blit(self.edu_label_7_2, (610,177))
    screen.blit(self.upgrade7_description, (610,194))
    screen.blit(self.display7_cost, (610,212))

    self.edu_label_8_1 = edu_font.render("Ensure Software", True, "#ffffff")
    self.edu_label_8_2 = edu_font.render("is Updated", True, "#ffffff")
    self.upgrade8_description = description_font.render(f"(+25 points per minute)", True, "#ffffff")
    self.display8_cost = cost_font.render(f"Cost: {str(self.upgrade8_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn8, border_radius=15)
    screen.blit(self.edu_label_8_1, (610,262))
    screen.blit(self.edu_label_8_2, (610,279))
    screen.blit(self.upgrade8_description, (610,296))
    screen.blit(self.display8_cost, (610,314))

    self.edu_label_9_1 = edu_font.render("White Hat Hacker", True, "#ffffff")
    self.edu_label_9_2 = edu_font.render("Assistance", True, "#ffffff")
    self.upgrade9_description = description_font.render(f"(+100 points per two minutes)", True, "#ffffff")
    self.display9_cost = cost_font.render(f"Cost: {str(self.upgrade9_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn9, border_radius=15)
    screen.blit(self.edu_label_9_1, (610,364))
    screen.blit(self.edu_label_9_2, (610,381))
    screen.blit(self.upgrade9_description, (610,398))
    screen.blit(self.display9_cost, (610,416))

    self.edu_label_10_1 = edu_font.render("Better Policy", True, "#ffffff")
    self.edu_label_10_2 = edu_font.render("from Corporate", True, "#ffffff")
    self.upgrade10_description = description_font.render(f"(+1000 points per five minutes)", True, "#ffffff")
    self.display10_cost = cost_font.render(f"Cost: {str(self.upgrade10_cost)}", True, "#ffffff")
    pygame.draw.rect(screen, "#488ebd", self.upgradeBtn10, border_radius=15)
    screen.blit(self.edu_label_10_1, (610,466))
    screen.blit(self.edu_label_10_2, (610,483))
    screen.blit(self.upgrade10_description, (610,500))
    screen.blit(self.display10_cost, (610,518))

  def draw_score(self):
    self.display_points = label_font.render(f"Cyber Points: {str(self.points)}", True, "#000000")
    screen.blit(self.display_points, (500, 565))

    self.display_points_per_click = label_font.render(f"{str(self.point_per_click)}: Cyber Points Per Click", True, "#000000")
    screen.blit(self.display_points_per_click, (0, 565))

  def click_buton(self):
    self.mouse_pos = pygame.mouse.get_pos()

    if self.mouse.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        self.clicked = True
      else:
        if self.clicked:
          self.points += self.point_per_click
          self.clicked = False

    if self.upgradeBtn1.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade1_cost:
          self.points -= self.upgrade1_cost
          self.upgrade1_cost *= 2
          self.point_per_click += 1

    if self.upgradeBtn2.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade2_cost:
          self.points -= self.upgrade2_cost
          self.upgrade2_cost *= 2
          self.point_per_click += 5

    if self.upgradeBtn3.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade3_cost:
          self.points -= self.upgrade3_cost
          self.upgrade3_cost *= 2
          self.point_per_click += 25

    if self.upgradeBtn4.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade4_cost:
          self.points -= self.upgrade4_cost
          self.upgrade4_cost *= 2
          self.point_per_click *= 2

    if self.upgradeBtn5.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade5_cost:
          self.points -= self.upgrade5_cost
          self.upgrade5_cost *= 10
          self.point_per_click *= 5

    if self.upgradeBtn6.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade6_cost:
          self.points -= self.upgrade6_cost
          self.upgrade6_cost *= 2
          self.autoMulti_1 += 1

    if self.upgradeBtn7.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade7_cost:
          self.points -= self.upgrade7_cost
          self.upgrade7_cost *= 2
          self.autoMulti_2 += 1

    if self.upgradeBtn8.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade8_cost:
          self.points -= self.upgrade8_cost
          self.upgrade8_cost *= 2
          self.autoMulti_3 += 1

    if self.upgradeBtn9.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade9_cost:
          self.points -= self.upgrade9_cost
          self.upgrade9_cost *= 2
          self.autoMulti_4 += 1

    if self.upgradeBtn10.collidepoint(self.mouse_pos):
      if pygame.mouse.get_pressed()[0]:
        if self.points >= self.upgrade10_cost:
          self.points -= self.upgrade10_cost
          self.upgrade10_cost *= 10
          self.autoMulti_5 += 1

    screen.blit(self.img, (self.mouse.x, self.mouse.y))
    screen.blit(self.wireImg, (self.wire.x, self.wire.y))

  def auto(self):
    if ((self.time % 10) == 0):
      self.points += (1 * self.autoMulti_1)

    if ((self.time % 30) == 0):
      self.points += (10 * self.autoMulti_2)

    if ((self.time % 60) == 0):
      self.points += (25 * self.autoMulti_3)

    if ((self.time % 120) == 0):
      self.points += (100 * self.autoMulti_4)

    if ((self.time % 300) == 0):
      self.points += (1000 * self.autoMulti_5)

    self.time += 0.02
    self.time = round(self.time, 2)

  def render(self):
    self.auto()
    self.click_buton()
    self.draw_score()
    self.upgrade()

pygame.init()

game = Game()

width = 800
height = 600
screen = pygame.display.set_mode(size=(width, height))

pygame.display.set_caption("Cyber_Clicker")

title_font = pygame.font.Font(None, 75)
label_font = pygame.font.Font(None, 45)
cost_font = pygame.font.Font(None, 30)
description_font = pygame.font.Font(None, 20)
edu_font = pygame.font.Font(None, 25)

title = title_font.render("Cyber Clicker", True, "#000000")
upgradeSet1 = label_font.render("PPC Upgrade:", True, "#000000")
upgradeSet2 = label_font.render("Auto Upgrade:", True, "#000000")

clock = pygame.time.Clock()
while True:
  screen.fill("#0000ff")
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.blit(title, (225, 0))
  screen.blit(upgradeSet1, (0, 0))
  screen.blit(upgradeSet2, (585, 0))

  game.render()

  pygame.display.update()
  clock.tick(50)
