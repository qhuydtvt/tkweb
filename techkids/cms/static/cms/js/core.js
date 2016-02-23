var TechKidsApp = (function($, undefined){
	var configs = {
		menuBreakPoint: 768
	}
	
	var menuOnHover = true;
	
	var init = function(){
		if(TechKidsApp.scrollSpy){
			TechKidsApp.scrollSpy.init();
		}
		
		$(window).resize(detectMenuModeChange);
	}
	
	var detectMenuModeChange = function(){
		if($(window).width() < menuBreakPoint){
			if(menuOnHover){
				$(".dropdown-toggle").each(function(){
					$(this).removeClass("disabled");
				}
				menuOnHover = false;
			});
		}
		else{
			if(!menuOnHover){
				$(".dropdown-toggle").each(function(){
					$(this).addClass("disabled");
				}
				menuOnHover = true;
			});
		}
	}
	
	return {
		init : init
	}
}(jQuery));

$(document).ready(function(){
	TechKidsApp.init();
});