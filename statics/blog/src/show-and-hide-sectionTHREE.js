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

				}else if(index == 1){
					
					forms[1].classList.add('show')

					forms[0].classList.remove('show')
				}

			}

		})
	})
})