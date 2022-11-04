from app import db

# Model
class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    rating = db.Column(db.Float)
    prep_time = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "prep_time": self.prep_time
        }
    # Construct a class method: take breakfast_dict and create a Breakfast instance
    @classmethod  # also remember the class decorator
    def from_dict(cls, breakfast_dict):
        return cls(
            name=breakfast_dict["name"],
            rating=breakfast_dict["rating"],
            prep_time=breakfast_dict["prep_time"]
        )

    # return cls or Breakfast here both works, the only difference is cls is more flexible, 
    # it also apply when there is another child class of Breakfast, cls could populate to the 
    # exact class we are using.
