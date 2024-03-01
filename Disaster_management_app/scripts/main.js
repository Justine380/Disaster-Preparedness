
const myImage = document.getElementById("myImage");
const imageSources = [
  "Disaster_management_app/Images/DisasterImages.png",
  // Add more image sources as needed
];
let currentIndex = 0;

myImage.onclick = () => {
  currentIndex = (currentIndex + 1) % imageSources.length;
  const newSrc = imageSources[currentIndex];
  myImage.setAttribute("src", newSrc);
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");