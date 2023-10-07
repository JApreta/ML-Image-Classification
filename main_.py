# # -*- coding: utf-8 -*-
# """
# Created on Sun Dec 12 13:00:19 2021
#
# @author: MontalJ
# """
#
# from pickle import load
# from numpy import argmax
# from keras.preprocessing.sequence import pad_sequences
# from keras.applications.vgg16 import VGG16
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.applications.vgg16 import preprocess_input
# from keras.models import Model
# from keras.models import load_model
# from gtts import gTTS
# import os
# import time
#
#
# # extract features from each photo in the directory
# def extract_features(filename):
#     # load the model
#     model = VGG16()
# 	# re-structure the model
#     model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
# 	# load the photo
#
#     image = load_img(filename, target_size=(224, 224))
#
#     # convert the image pixels to a numpy array
#     image = img_to_array(image)
# 	# reshape data for the model
#
#     image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# 	# prepare the image for the VGG model
#
#     image = preprocess_input(image)
# 	# get features
#
#     feature = model.predict(image, verbose=0)
#
#     return feature
#
# # map an integer to a word
# def word_for_id(integer, tokenizer):
# 	for word, index in tokenizer.word_index.items():
# 		if index == integer:
# 			return word
# 	return None
#
# # generate a description for an image
# def generate_desc(model, tokenizer, photo, max_length):
# 	# seed the generation process
# 	in_text = 'startseq'
# 	# iterate over the whole length of the sequence
# 	for i in range(max_length):
# 		# integer encode input sequence
# 		sequence = tokenizer.texts_to_sequences([in_text])[0]
# 		# pad input
# 		sequence = pad_sequences([sequence], maxlen=max_length)
# 		# predict next word
# 		yhat = model.predict([photo,sequence], verbose=0)
# 		# convert probability to integer
# 		yhat = argmax(yhat)
# 		# map integer to word
# 		word = word_for_id(yhat, tokenizer)
# 		# stop if we cannot map the word
# 		if word is None:
# 			break
# 		# append as input for generating the next word
# 		in_text += ' ' + word
# 		# stop if we predict the end of the sequence
# 		if word == 'endseq':
# 			break
# 	return in_text
#
# # load the tokenizer
# tokenizer = load(open('tokenizer.pkl', 'rb'))
# # pre-define the max sequence length (from training)
# max_length = 34
# # load the model
# # model = load_model('model-ep002-loss3.245-val_loss3.612.h5')
# model = load_model('model-ep004-loss3.536-val_loss3.876.h5')
# # load and prepare the photograph
# image_name = '1.jpg'
# photo = extract_features(image_name)
# # generate description
# description = generate_desc(model, tokenizer, photo, max_length)
#
#
#
#
#
#
#
# # Display the image
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# img = mpimg.imread(image_name)
# imgplot = plt.imshow(img)
# plt.show()
#
#
#
#
#
#
#
# # The text that you want to convert to audio
# mytext = description.replace("startseq", "")
# mytext = mytext.replace("endseq", "")
# mytext = mytext.strip()
# mytext = mytext.upper()
# print('\n \nEnglish')
# print(mytext)
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text = mytext, lang = language, slow = True)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save(image_name + "english.mp3")
#
# time.sleep(3)
# # Playing the converted file
# os.system(image_name + "english.mp3")
#
#
# time.sleep(10)
# from translate import Translator
# translator= Translator(to_lang = "zh")
# translation = translator.translate(mytext)
# print('\nMainland China')
# print(translation)
# myobj = gTTS(text = translation, lang = 'zh-CN', slow = True)
# myobj.save(image_name + "Main_China.mp3")
# time.sleep(3)
# os.system(image_name + "Main_China.mp3")
