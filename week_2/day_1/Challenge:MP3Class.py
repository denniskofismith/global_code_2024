class mp3playlist:
    tracks = []
        

    def load_playlist(self):

        f = open("tracks.txt","x")
        
        for x in f:
            self.tracks.append(x)
            
        
        
    def display_tracks(self):

        for t in self.tracks:
            print(t)       

    def add_playlist(self,playlist):
        
        self.tracks.append(playlist)
        
    def remove_playlist(self,playlist=str):
        index = self.tracks.index(playlist)
        self.tracks.pop(index)
        
    def count_numbs_tracks(self):
        
        lenght = len(self.tracks)
        
        return lenght
    
    def is_empty(self):
        
        if len(self.tracks) is not 0:
            return False
            
        else:
            return True
    
    def clear_reset(self):
        
        if self.is_empty() == True:
            print("Playlist empthy")
            
        self.tracks.clear()
        
tracks1 = mp3playlist()


tracks1.load_playlist()


tracks1.add_playlist("drugs you should not try")
tracks1.count_numbs_tracks()
tracks1.display_tracks()


