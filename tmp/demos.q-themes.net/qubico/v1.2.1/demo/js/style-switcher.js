$(document).ready(function(){

	var slidersHTML = '<h1>Choose Slider</h1>\
		<a href="index.html"><p><img src="switcher_thumb1.png" alt="">Multilayer Slider</p></a>\
		<a href="perspective-slider.html"><p><img src="switcher_thumb2.png" alt="">Perspective Slider</p></a>\
		<a href="idevices-slider.html"><p><img src="switcher_thumb3.png" alt="">iDevices Slider</p></a>'
		
	$(slidersHTML).insertAfter('#toggle-switcher');

	$('#toggle-switcher').click(function(){
		if($(this).hasClass('opened')){
			$(this).removeClass('opened');
			$('#style-switcher').animate({'right':'-222px'});
		}else{
			$(this).addClass('opened');
			$('#style-switcher').animate({'right':'-10px'});
		}
	});
	
	$('#style-switcher li').click(function(e){
		e.preventDefault();
		
		$elem = $(this);
		
		$('link#theme').attr('href', 'css/qubico-'+$elem.attr('id')+'.css');
		
		$('.logo-small img').attr('src', 'assets/logo-small-'+$elem.attr('id')+'.png');
		
		$('link#theme').load(function(){
			$('link#main').attr('href', 'css/qubico-'+$elem.attr('id')+'.css');
		});
		
	});
});