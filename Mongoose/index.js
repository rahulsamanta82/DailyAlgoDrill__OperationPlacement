const mongoose = require('mongoose');

main()
   .then((res)=>{
    console.log("connection succesful");
  })
  .catch(err => console.log(err));

async function main() {
  await mongoose.connect('mongodb://127.0.0.1:27017/test');

  // use `await mongoose.connect('mongodb://user:password@127.0.0.1:27017/test');` if your database has auth enabled
}

const userSchema= new mongoose.Schema({
    name:String,
    email:String,
    age:Number
});
const User = mongoose.model("User", userSchema);
// const Emplyee = mongoose.model("Emplyee", userSchema);
// const user2=new User({
//     name:"Rahul",
//     email:"rs4655742@gmail.com",
//     age:48
// })

// user2
// .save()
// .then((res)=>{
//     console.log(res);
// })
// .catch((err)=>{
//     console.log(err);
// });

// User.insertMany([
//     {name:"soumen", email:"rs4893023@gmail.com", age:35},
//     {name:"sourav", email:"rahul54646@gmail.com", age:39},
// ]).then((res)=>{
//     console.log(res);
// });

User.find({age:{$gt: 650}},{age:750})
    .then((res)=>{
    console.log(res);
});


// User.updateOne({name:"sourav"},{age: 700})
// .then((res)=>{
//   console.log(res);
// })
