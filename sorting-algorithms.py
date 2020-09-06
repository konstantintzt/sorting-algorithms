import random
import math
import pygame
import argparse
import os
import sys
import itertools

# Arguments parsing
parser = argparse.ArgumentParser(description="Sorting algorithms visualization by Broksy")
parser.add_argument("--output", action="store_true")
args = parser.parse_args()

# White RGB constant (used for texts)
WHITE = (255,255,255)

# INSERTION SORT O(n^2)
def insertion_sort(a):
    for i in range(len(a)-1):
        if a[i+1]<a[i]:
            j=i
            while j>=0 and a[j+1]<a[j]:
                a[j], a[j+1] = a[j+1], a[j]
                j-=1
        draw_array(a, (0,0,155), "Insertion sort: O(n²)", "6.348s")

# SELECTION SORT O(n^2)
def selection_sort(a):
    sorted_index = 0
    for i in range(len(a)):
        mni = i
        for j in range(i+1, len(a)):
            if a[j]<a[mni]:
                mni = j
        draw_array(a, (0,155,0), "Selection sort: O(n²)", "3.350s")
        a[mni], a[i] = a[i], a[mni]

# BUBBLE SORT O(n^2)
def bubble_sort(a):
    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                swap = True
                a[i+1], a[i] = a[i], a[i+1]
        draw_array(a, (155, 0, 0), "Bubble sort: O(n²)", "12.131s")

# BOGOSORT (don't ever use this, it's the worst thing) O(n*n!)
def bogosort(a):
    for p in itertools.permutations(a):
        ok = True
        for i in range(len(p)-1):
            if p[i]>p[i+1]:
                ok = False
                break        
        draw_array(p, (0,155,155), "Bogosort: O(n*n!)", "Incredibly long")
        if ok:
            return

# PANCAKE SORT O(n^2)
def pancake_sort(a):
    cur = len(a)
    while cur:
        mni = 0
        for i in range(cur):
            if a[i]>a[mni]:
                mni = i   

        pancake_flip(a, mni)
        pancake_flip(a, cur-1)
        draw_array(a, (155,155,155), "Pancake sort: O(n²)", "14.548s")
        cur-=1

def pancake_flip(a, ind):
    for i in range(ind):
        a[i], a[ind-i] = a[ind-i], a[i]

# COCKTAIL SORT O(n^2)
def cocktail_sort(a):
    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                swap = True
                a[i+1], a[i] = a[i], a[i+1]
        draw_array(a, (135,12,64), "Cocktail sort: O(n²)", "8.151s")
        if not swap:
            break
        for i in range(len(a)-1, 1, -1):
            if a[i]<a[i-1]:
                swap = True
                a[i], a[i-1] = a[i-1], a[i]
        draw_array(a, (135,12,64), "Cocktail sort: O(n²)", "8.151s")

# QUICKSORT O(n*log(n))
def quicksort(a, l=0, r=None):
    if r is None:
        r = len(a)-1
    if l < r:
        p = partition(a,l,r)
        quicksort(a, l, p-1)
        quicksort(a, p+1, r)

# Helper function for quicksort
def partition(a, l, r):
    draw_array(a, (23,145,64), "Quicksort: O(n*log(n))", "0.026s")
    i = l-1
    pivot = a[r]
    for j in range(l,r):
        if a[j] < pivot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[r] = a[r], a[i+1]
    draw_array(a, (23,145,64), "Quicksort: O(n*log(n))", "0.026s")
    return i+1


# Function to represent array as bars
def draw_array(arr, base_color, title, time):
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    n = len(arr)

    # Texts to be displayed
    title_text = font.render(title, True, WHITE)
    time_text = small_font.render(str(time)+" for 10 000 numbers", True, WHITE)

    # Clear screen
    window.fill((0,0,0))

    # Draw array as bars
    for i in range(n):
        rect = pygame.Rect(round(i/n*1920), 1080-round(arr[i]/n*1080), round(1920/n), round(arr[i]/n*1080))
        color_change = round(arr[i]/n*100)
        color = tuple(channel+color_change for channel in base_color)
        pygame.draw.rect(window, color, rect)
    
    # Add text and update
    window.blit(title_text, (20,20))
    window.blit(time_text, (20, 80))
    pygame.display.update()

    # Save frame if required
    if args.output:
        pygame.image.save(window, f"./out/frame_{frame_number}.jpg")
        frame_number+=1


# Preparation for image sequence output
if args.output:    
# Check if output directory exists, and create it if it doesn't
    if not os.path.exists("./out"):
        os.mkdir("./out")
    frame_number=0

# Pygame initialization
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 48, italic=True)
small_font = pygame.font.SysFont("Times New Roman", 32, italic=True)
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Broksy's sorting algorithms visualization")
clock = pygame.time.Clock()

# Array initialization (960 elements = every element is 2px wide)
nums = [i for i in range(1,961)]

# Animation start

random.shuffle(nums)
insertion_sort(nums)

random.shuffle(nums)
selection_sort(nums)

random.shuffle(nums)
bubble_sort(nums)

random.shuffle(nums)
pancake_sort(nums)

random.shuffle(nums)
cocktail_sort(nums)

random.shuffle(nums)
quicksort(nums)

nums = [i for i in range(1,7)]  # If i were to use a larger array, bogosort would take too long

random.shuffle(nums) 
bogosort(nums)

# Animation end

pygame.quit()