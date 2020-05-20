$(function() {

//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function(){
/* Prevent empty fields */
let inputs = document.getElementById(`fieldset${event.target.id}`).getElementsByTagName('input');

let len = inputs.length - event.target.id;   //removing buttons from length

 for(let i=0; i<len; i++){
    if(!inputs[i].value){
            inputs[i].focus();
            inputs[i].style.outline = '1px solid red';
            inputs[i].classList.add('error');
            inputs[i].addEventListener('keydown', ()=>{
                  inputs[i].style.outline = 0;
                  inputs[i].style.color = 'black';

                  inputs[i].classList.remove('error');

            });
         return false;
     }
  }
 if(event.target.id == 1){
        /* Confirm roll is a number */
let roll = inputs[0].value;
let rollPattern = /^\d+$/;
 if(!rollPattern.test(roll)){

      inputs[0].value = '';
      inputs[0].placeholder = `${roll} is not a valid roll number`;
      inputs[0].focus();
      inputs[0].style.outline = '1px solid red';
      inputs[0].classList.add('error');
      inputs[0].addEventListener('keydown', ()=>{
        inputs[0].style.outline = 0;
        inputs[0].style.color = 'black';
        inputs[0].classList.remove('error');
        inputs[0].placeholder = 'Enter your roll number eg: 181522';
    })
     return false;
 }


 }


	if(animating) return false;
	animating = true;

	current_fs = $(this).parent();
	next_fs = $(this).parent().next();

	//activate next step on progressbar using the index of next_fs
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

	//show the next fieldset
	next_fs.show();
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale current_fs down to 80%
			scale = 1 - (1 - now) * 0.2;
			//2. bring next_fs from the right(50%)
			left = (now * 50)+"%";
			//3. increase opacity of next_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'transform': 'scale('+scale+')'});
			next_fs.css({'left': left, 'opacity': opacity});
		},
		duration: 800,
		complete: function(){
			current_fs.hide();
			animating = false;
		},
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".previous").click(function(){
	if(animating) return false;
	animating = true;

	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();

	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

	//show the previous fieldset
	previous_fs.show();
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale previous_fs from 80% to 100%
			scale = 0.8 + (1 - now) * 0.2;
			//2. take current_fs to the right(50%) - from 0%
			left = ((1-now) * 50)+"%";
			//3. increase opacity of previous_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'left': left});
			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
		},
		duration: 800,
		complete: function(){
			current_fs.hide();
			animating = false;
		},
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".submit").click(function(){
event.preventDefault();
let inputs = document.getElementById(`fieldset${event.target.id}`).getElementsByTagName('input');
let len = inputs.length - 2;   //removing buttons from length

 for(let i=0; i<len; i++){
     if(!inputs[i].value){
            inputs[i].focus();
            inputs[i].style.outline = '1px solid red';
            inputs[i].classList.add('error');
               inputs[i].addEventListener('keydown', ()=>{
              inputs[i].style.outline = 0;
              inputs[i].style.color = 'black';
              inputs[i].classList.remove('error');

            });

            return false;

     }
  }


  let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  let email = inputs[0].value;

  if(!emailPattern.test(email)){
      inputs[0].value = '';
      inputs[0].placeholder = `${email} is not valid email`;
      inputs[0].focus();
      inputs[0].style.outline = '1px solid red';
      inputs[0].classList.add('error');
      inputs[0].addEventListener('keydown', ()=>{
       inputs[0].style.outline = 0;
       inputs[0].style.color = 'black';
       inputs[0].classList.remove('error');
       inputs[0].placeholder = 'Enter your email';
      })
     return false;
  }


  let password = inputs[1].value;
  let password1 = inputs[2].value;
  let pswdError = document.getElementById('pswd-error');
  let confirmPswdError = document.getElementById('confirm-pswd-error');


  if(password.length < 5 || password.indexOf(' ')>=0){
     pswdError.textContent = 'Password must be at least 5 characters long with no spaces';
     inputs[1].focus();
     inputs[1].style.outline = '1px solid red';

  inputs[1].addEventListener('keydown', ()=>{
    pswdError.textContent = '';
    inputs[1].style.outline = '';
    confirmPswdError.textContent = '';
    inputs[2].style.outline = '';
  })

     return false;

  }

  /* check whether two pswds are same or not */
  if(password !== password1){
        confirmPswdError.textContent = "Passwords didn't match";
        inputs[2].focus();
        inputs[2].style.outline = '1px solid red';

        inputs[2].addEventListener('keydown', ()=>{
              confirmPswdError.textContent = '';
              inputs[2].style.outline = '';
        })

    return false;
  }




})

});
