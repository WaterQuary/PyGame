import time
loading_char = "█"
bar_len = 50

def get_top_text(title):
    left_pad = (bar_len - len(title)) // 2
    right_pad = bar_len - len(title) - left_pad
    return "╔" + ("═" * left_pad) + title + ("═" * right_pad) + "╗"

bottom_text = "╚" + ("═" * bar_len) + "╝"
def run_loading_bar():
    top_text = get_top_text("Загрузка")
    

    for i in range(bar_len + 1):
  
        bar = (loading_char * i) + (" " * (bar_len - i))
        
        result = f"\r{top_text}\n║{bar}║\n{bottom_text}"
        print(result, end = "", flush= True)  
        if i == bar_len // 2 + 3:
            time.sleep(2)
        elif i == bar_len - 2:
            time.sleep(3)
        else:
            time.sleep(0.02)
        if i < bar_len:
            print("\x1b[2A", end="")