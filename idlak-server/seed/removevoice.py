#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import argparse
import xmltodict
from app import app, db
from app.models.voice import Voice

parser = argparse.ArgumentParser(description='Remove a voice from the database.')
parser.add_argument('-i', help='id of the voice')

def removeVoice():
    args = vars(parser.parse_args())
    errs = ""
    if args['i'] is None:
        errs += ", id"

    if len(errs) > 0:
        errs = errs[2:]
        print("Please provide {} of the voice".format(errs))
        sys.exit()
        
    voice_id = args['i']
    voice = Voice.query.filter_by(id=voice_id).first()
    voice.delete()

    print("Voice has been deleted:\n{{\n"
                            "\tid: {}\n"
                            "\tname: {}\n"
                            "\tlanguage: {}\n"
                            "\taccent: {}\n"
                            "\tgender: {}\n"
                            "\tdirectory: {}\n}}"
                            .format(voice.id, voice.name, voice.language, voice.accent, voice.gender, voice.directory))

if __name__ == '__main__':
    removeVoice()