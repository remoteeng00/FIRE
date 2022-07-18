def new_jobs(self):
    import glob, os
    
    files = glob.glob(os.path.join(self.data_folder,"*.txt"))
    #self.logger.info("Parallelizing per file: %s" % files)
    return [(f,) for f in files]
