#Hi i am readme

1- Environment Variables: Ensure your environment variables (like FLASK_APP) are set correctly.
   You can set them in your terminal:
    export FLASK_APP=main.py  # On macOS/Linux
    set FLASK_APP=main.py     # On Windows

2- To run migration ---
    flask db init
    flask db migrate -m "Your migration message"
    flask db upgrade

3- Mysql Database uri--
    SQLALCHEMY_DATABASE_URI= f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
4- Create
      session.add(User(name='Alice', email='alice@example.com')); session.commit()
   Read   
      user = session.query(User).filter_by(name='Alice').first(); print(user.name, user.email)
   Update
      user = session.query(User).filter_by(name='Alice').first(); user.email = 'alice@newdomain.com'; session.commit()
   Delete
      user = session.query(User).filter_by(name='Alice').first(); session.delete(user); session.com
