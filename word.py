import os
import tkinter
import wordcloud
from tkinter import filedialog
from matplotlib import pyplot as plt


# This is the uploader

def _upload():

    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window

    currdir = os.getcwd()
    sourcefile = filedialog.askopenfilename(
        parent=root, initialdir=currdir, title='Please select a file',
        filetype=(("Text Files", "*.txt"), ("All Files", "*")))
    return open(sourcefile).read()


def calculate_frequencies(file_contents):

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that",
                           "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    file_contents2 = ""
    for char in file_contents:
        if char.isalpha() == True or char.isspace():
            file_contents2 += char

    file_contents2 = file_contents2.split()
    file_without_uninteresting_words = []

    for word in file_contents2:
        if word.lower() not in uninteresting_words and word.isalpha() == True:
            file_without_uninteresting_words.append(word)

    frequencies = {}

    for word in file_without_uninteresting_words:
        if word.lower() not in frequencies:
            frequencies[word.lower()] = 1
        else:
            frequencies[word.lower()] += 1

    # wordcloud
    cloud = wordcloud.WordCloud(background_color="white")
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# If you have done everything correctly, your word cloud image should appear after running the cell below.  Fingers crossed!

myimage = calculate_frequencies(_upload())
plt.imshow(myimage, interpolation='bilinear')
plt.axis('off')
plt.show()
