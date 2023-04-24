class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


class Box():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)


class SoulBox():
	def __init__(self, image, soul_icon, pos, skill, description, soul_cost, skill_font, description_font, soul_cost_font, base_color, hovering_color):
		self.image = image
		self.soul_icon = soul_icon
		self.skill = skill
		self.description = description
		self.soul_cost = soul_cost
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.skill_font = skill_font
		self.description_font = description_font
		self.soul_cost_font = soul_cost_font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.skill_text = self.skill_font.render(self.skill, True, self.base_color)
		self.description_text = self.description_font.render(self.description, True, self.base_color)
		self.soul_cost_text = self.soul_cost_font.render(self.soul_cost, True, self.base_color)
		if self.image is None:
			pass
			# self.image = self.skill_text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.skill_text_rect = self.image.get_rect(midleft=(self.x_pos - 270, self.y_pos + 12))
		self.description_text_rect = self.image.get_rect(midleft=(self.x_pos-60, self.y_pos + 16))
		self.soul_cost_text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		soul_cost_text_rect_deviation = self.soul_cost_text.get_rect()
		self.soul_cost_text_rect.left = self.rect.right - soul_cost_text_rect_deviation.right - 10  # Ajuste o valor 10 para a margem desejada
		self.soul_cost_text_rect.top = self.rect.top + 10
		self.soul_icon_rect = self.image.get_rect(midleft=(self.x_pos-340, self.y_pos+5))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.skill_text, self.skill_text_rect)
		screen.blit(self.description_text, self.description_text_rect)
		screen.blit(self.soul_cost_text, self.soul_cost_text_rect)
		screen.blit(self.soul_icon, self.soul_icon_rect)


	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False


	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.skill_text = self.skill_font.render(self.skill, True, self.hovering_color)
			self.soul_cost_text = self.soul_cost_font.render(self.soul_cost, True, self.hovering_color)
			# self.description_text = self.description_font.render(self.description, True, self.hovering_color)
		else:
			self.skill_text = self.skill_font.render(self.skill, True, self.base_color)
			self.soul_cost_text = self.soul_cost_font.render(self.soul_cost, True, self.base_color)
			# self.description_text = self.description_font.render(self.description, True, self.base_color)





