// tabs boxes
let tabs = document.querySelectorAll('.TABS > div');
let forms = document.querySelectorAll('.forms');

// start write event
tabs[0].classList.add('active');
forms[0].classList.add('show');
tabs.forEach(tab => {
	tab.addEventListener('click' , e => {
		let tabsTwo = document.querySelectorAll('.TABS > div');
		tabsTwo.forEach((tabTwo  , index )=> {
			if(tabTwo != tab){
				tabTwo.classList.remove('active');
			}else if(tabTwo == tab){
				
				tabTwo.classList.add('active');

				if(index == 0){

					forms[0].classList.add('show')

					forms[1].classList.remove('show')
					forms[2].classList.remove('show')
					forms[3].classList.remove('show')
					forms[4].classList.remove('show')
					forms[5].classList.remove('show')

				}else if(index == 1){
					
					forms[1].classList.add('show')

					forms[0].classList.remove('show')
					forms[2].classList.remove('show')
					forms[3].classList.remove('show')
					forms[4].classList.remove('show')
					forms[5].classList.remove('show')
				}else if(index == 2){
					forms[2].classList.add('show')

					forms[0].classList.remove('show')
					forms[1].classList.remove('show')
					forms[3].classList.remove('show')
					forms[4].classList.remove('show')
					forms[5].classList.remove('show')
				}else if(index == 3){
					forms[3].classList.add('show')

					forms[0].classList.remove('show')
					forms[1].classList.remove('show')
					forms[2].classList.remove('show')
					forms[4].classList.remove('show')
					forms[5].classList.remove('show')
				}else if(index == 4){
					forms[4].classList.add('show')

					forms[0].classList.remove('show')
					forms[1].classList.remove('show')
					forms[2].classList.remove('show')
					forms[3].classList.remove('show')
					forms[5].classList.remove('show')

				}else if(index == 5){
					forms[5].classList.add('show')

					forms[0].classList.remove('show')
					forms[1].classList.remove('show')
					forms[2].classList.remove('show')
					forms[3].classList.remove('show')
					forms[4].classList.remove('show')

				}

			}

		})
	})
})