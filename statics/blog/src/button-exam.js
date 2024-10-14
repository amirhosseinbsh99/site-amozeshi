// defined variables
let sliders = document.querySelectorAll('.form');
let goNext = document.querySelector('.goNextBtn');
let goPrev = document.querySelector('.goPrevBtn');
let resultBtn = document.querySelector('.myBtn');
var active = 0

sliders[active].classList.add('active')

if (active==0){
	goPrev.classList.add('d-none')
}

goNext.addEventListener('click' , ()=>{
	sliders.forEach((slider , index)=>{
		if (slider.classList.contains("active")){
			slider.classList.remove("active")
			active = index + 1
		}

		if (active == sliders.length-1){
			resultBtn.classList.remove('d-none')
			resultBtn.classList.add('active')
			goNext.classList.add('d-none')
		} 
	});
	sliders[active].classList.add('active')

	if (active!=0){
		goPrev.classList.remove('d-none')
	}

})
goPrev.addEventListener('click' , ()=>{
	sliders.forEach((slider , index)=>{

		if (slider.classList.contains("active")  ){
			slider.classList.remove("active")
			active = index - 1
		}
		
		if (active == sliders.length-1){
			resultBtn.classList.add('active')
			goNext.classList.add('d-none')
		} 
	});
	sliders[active].classList.add('active')
	if (active != sliders.length-1){
		resultBtn.classList.add('d-none')
		goNext.classList.remove('d-none')
	} 
	if (active == sliders.length-1){
		resultBtn.classList.add('active')
		goNext.classList.add('d-none')
	}

	if (active==0){
		goPrev.classList.add('d-none')
	}

})
