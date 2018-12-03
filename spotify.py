# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:59:55 2018

@author: simon
"""

import spotipy
import spotipy.util as util
from pprint import pprint
import json

def make_spotify():
    '''
    make instance of authorized spotify api client with my details
    
    returns instance object
    '''
    with open('secret.json') as f:
        data = json.load(f)
        
    scope = data['scopes']
    username = data['username']
    client_id = data['client_id']
    client_secret = data['client_secret']
    redirect_uri = data['redirect_uri']
    
    token = util.prompt_for_user_token(
            username, 
            scope, 
            client_id=client_id, 
            client_secret=client_secret,
            redirect_uri=redirect_uri
            )
    
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print("Couldn't authorize")
        
    return sp
    


if __name__ == '__main__':
    sp = make_spotify()
    
    
    top_artists = sp.current_user_top_artists()
    top_tracks = sp.current_user_top_artists()
    

    
