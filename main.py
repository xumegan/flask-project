from website import create_app
app=create_app()

if __name__=='__main__':
  app.run(debug=True) # this means every time there is changes it will rerun server when run production need to turn off

