#!/usr/bin/env python3
import turtle;
import _thread as thread, time;
import sys, os;
import random;

regie = turtle.Turtle ();
regie.shape ('turtle');
my_win = turtle.Screen ();

def play (filename):
	command = 'mpg123 ' + filename;
	os.system (command);

def traverse (my_turt, line_length):
	if (line_length < 400):
		my_turt.forward (line_length);
		my_turt.right (random.randint (40, 300));
		traverse (my_turt, line_length + 5);

def start_process ():
	thread.start_new_thread (traverse, (regie, 50));
	thread.start_new_thread (play, ('insect_sound.mp3',));
	my_win.exitonclick ();


if (__name__ == '__main__'):
	start_process ();
