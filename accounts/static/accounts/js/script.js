
 //jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches
var authToken = '';


function slideForward(target){

  if(animating) return false;
	animating = true;

	current_fs = target.parent();
	next_fs = target.parent().next();

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


}

function slideBackward(target){
    if(animating) return false;
	animating = true;

	current_fs = target.parent();
	previous_fs = target.parent().prev();

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
}


$(".previous").click(function(){
   slideBackward($(this));
});

$("#next1").click(function(){

let rollField = document.getElementById('roll');
let roll = rollField.value;
let rollErrorField = document.getElementById('roll-error');
let nextBtn = event.target;

if(isEmpty(roll)){
  displayError(rollField, rollErrorField, 'Roll is a required field');
  return false;
}

if(isInvalid(roll)){
  displayError(rollField, rollErrorField, `${roll} is not a valid roll number`);
  return false;
}

/* send ajax request */

    let rollData =  {
                      roll: parseInt(roll)  };
    loadGif(nextBtn);
    rollField.disabled = true;
    let response = postData('/accounts/roll/', rollData)

    response
    .then(data => {
        if(data.success){
             slideForward($(this));
             resetGif(nextBtn, 'Next');
             reset(rollField, rollErrorField);
             rollField.disabled = false;
        }else{
            resetGif(nextBtn, 'Next');
            rollField.disabled = false;
            displayError(rollField, rollErrorField, data.msg)
        }

    })
    .catch(error=>{
        console.log(error);
        resetGif(nextBtn, 'Next');
        rollField.disabled = false;
        displayError(rollField, rollErrorField, "Something went wrong.");
        passwordConfirmField.style.outline = '';


 })


});


$("#next2").click(function(){


    let codeField = document.getElementById('code');
    let code = codeField.value;
    let codeErrorField = document.getElementById('code-error');
    let nextBtn = event.target;


    if(isEmpty(code)){
         displayError(codeField, codeErrorField, 'Verification is a required field');
         return false;
   }

   /* send ajax request */
   console.log(parseInt(code));
   let codeData = {
      roll: parseInt(document.getElementById('roll').value),
      code: parseInt(code)
   }
   loadGif(nextBtn);
   codeField.disabled = true;
   let response = postData('/accounts/verify/', codeData)

   response
   .then(data => {
        if(data.success){
             authToken = data.token;
             console.log(authToken);
             slideForward($(this));
             resetGif(nextBtn, 'Next');
             reset(codeField, codeErrorField);
             codeField.disabled = false;
        }else{
            resetGif(nextBtn, 'Next');
            codeField.disabled = false;
            console.log(data)
            displayError(codeField, codeErrorField, data.msg)
        }

    })
    .catch(error=>{
        console.log(error);
        resetGif(nextBtn, 'Next');
        codeField.disabled = false;
        displayError(codeField, codeErrorField, "Something went wrong.");
        passwordConfirmField.style.outline = '';


 })

});

$("#submit").click(function(){
event.preventDefault();

let passwordField = document.getElementById('password');
let passwordConfirmField = document.getElementById('password-confirm');
let passwordFieldError = document.getElementById('pswd-error');
let passwordConfirmFieldError = document.getElementById('confirm-pswd-error');
let password = passwordField.value;
let password1 = passwordConfirmField.value;
let submitBtn = event.target;

if(isEmpty(password)){
    displayError(passwordField, passwordFieldError, 'Password is a required field');
    passwordField.addEventListener('keydown', ()=>{
       reset(passwordField, passwordFieldError);
    });
    return false;
}

if(isEmpty(password1)){
  displayError(passwordConfirmField, passwordConfirmFieldError, 'Confirmation Password is a required field');
  passwordConfirmField.addEventListener('keydown', ()=>{
       reset(passwordConfirmField, passwordConfirmFieldError);
    });

  return false;
}

if(containsSpaces(password)){
   displayError(passwordField, passwordFieldError, 'Password must not contain spaces');
   return false;
}

if(isShort(password)){
   displayError(passwordField, passwordFieldError, 'Password must be at least 5 characters long');
   return false;
}

if(!matches(password, password1)){
   displayError(passwordConfirmField, passwordConfirmFieldError, "Passwords didn't match");
   passwordConfirmField.addEventListener('keydown', ()=>{
       reset(passwordConfirmField, passwordConfirmFieldError);
   });
   passwordField.addEventListener('keydown', ()=>{
       reset(passwordConfirmField, passwordConfirmFieldError);
   });

  return false;

}
 /* ajax request */
 loadGif(submitBtn);
 passwordField.disabled = true;
 passwordConfirmField.disabled = true;

 let studentData = {
    roll: parseInt(document.getElementById('roll').value),
    password : password,
    token: authToken
 }

 console.log(studentData);

 let response = postData('/accounts/register/', studentData);

 response
 .then(data => {
     if(data.success){
        console.log(data);
        resetGif(submitBtn, 'Submit');
        passwordField.disabled = false;
        passwordConfirmField.disabled = false;
        window.location.href = '/accounts/student-home/';
     }else{
        resetGif(submitBtn, 'Submit');
        passwordField.disabled = false;
        passwordConfirmField.disabled = false;
        displayError(passwordConfirmField, passwordConfirmFieldError, data.msg);
        passwordConfirmField.style.outline = '';

     }

 })
 .catch(error=>{
        console.log(error);
        resetGif(submitBtn, 'Submit');
        passwordField.disabled = false;
        passwordConfirmField.disabled = false;
        displayError(passwordConfirmField, passwordConfirmFieldError, "Something went wrong.");
        passwordConfirmField.style.outline = '';


 })

});



function isEmpty(roll){
  if(!roll) return true;
}

function isInvalid(roll){
    let numberPattern = /^\d+$/;
    if(!numberPattern.test(roll)) return true;
}

function isShort(password){
   if(password.length < 5) return true;
}

function containsSpaces(password){
  if(password.indexOf(' ') >= 0) return true;
}


function displayError(inputField, errorField, errorMsg){
  inputField.style.outline = '1px solid red' ;
  inputField.focus();
  errorField.style.fontFamily = 'Raleway';
  errorField.style.fontWeight = '600';
  errorField.textContent = errorMsg;
  errorField.style.display = 'block';
}

function reset(inputField, errorField){
  inputField.style.outline = '' ;
  errorField.textContent = '';
  errorField.style.display = 'none';
}

function matches(password, password1){
  if(password === password1) return true;
}

async function postData(url, data){
  let response =  await fetch(url,{
       method : 'POST',
       headers: {'Content-Type': 'application/json'},
       body: JSON.stringify(data)
    })
    .then(response => response.json());

   return response;

}

function loadGif(btn){
  btn.innerHTML = `<i  style="font-size:25px;" class="fa fa-spinner fa-spin mr-1"></i>`
  btn.disabled = true;
}

function resetGif(btn,value){
  btn.innerHTML = value;
  btn.disabled = false;
}