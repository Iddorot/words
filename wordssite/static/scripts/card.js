function flip_card(cards) {
  cards.forEach((card)=>{
    card.addEventListener( 'click', function(){
      card.classList.toggle('is-flipped');
    });
  })}

window.onload = () => {
  var cards = document.querySelectorAll('.card');
  flip_card(cards)
};
