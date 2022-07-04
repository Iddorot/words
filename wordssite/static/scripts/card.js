console.log("are we loading?")
function flip_card(cards) {
  cards.forEach((card)=>{
    card.addEventListener( 'click', function(){
      card.classList.toggle('is-flipped');
    });
  })}

window.onload = () => {
  console.log("yes")
  var cards = document.querySelectorAll('.card');
  flip_card(cards)
};
