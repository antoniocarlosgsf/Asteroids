from pygame.image import load

def load_sprite(nome, alpha=True):
    path = f'imagens/{nome}.png'
    loaded_sprite = load(path)

    if alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
    
    