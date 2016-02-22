var TechKidsApp = (function($, undefined){
	
	var configs = {
		skinWidth: 100,
		animateClasses : [
			"fade_up",
			"fade_left",
			"fade_right",
			"fade_scale",
		],
		animateOffSuffix : "_off",
		animateTransitionClass : "animate_fade"
	}
	
	var scrollThrotte = false;
	var viewportHeight = 0;
	
	var init = function(){
		$(window).bind("resize", calculateViewportHeight);
		calculateViewportHeight();
		
		initFadeElements();
		
		$(window).bind("scroll",scrollSpy);
		
		setTimeout(lateInitFadeElements, 100);
	}
	
	var calculateViewportHeight = function(){
		viewportHeight = $(window).height() - configs.skinWidth;
		if(viewportHeight < 0) viewportHeight = 0;
	}
	
	var scrollSpy = function(){
		if($(window).scrollTop() > 0 && scrollThrotte) return;
		if(!scrollThrotte){
			scrollThrotte = true;
			setTimeout(function(){scrollThrotte = false}, 100);
		}
		
		// Nav
		if($(window).scrollTop() > 100){
			$("#main_nav").removeClass("navbar_at_top");
		}
		else if(!$("#main_nav").hasClass("navbar_at_top")){
			$("#main_nav").addClass("navbar_at_top");
		}
		
		configs.animateClasses.forEach(function(theClass){
			$("."+ theClass + configs.animateOffSuffix).each(function(){
				if($(this).offset().top > $(window).scrollTop() && $(this).offset().top < $(window).scrollTop() + viewportHeight){
					$(this).removeClass(theClass + configs.animateOffSuffix);
				}
			});
		});
	}
	
	var initFadeElements = function(){
		configs.animateClasses.forEach(function(theClass){
			$("."+theClass).each(function(){
				$(this).addClass(theClass + configs.animateOffSuffix);
				
				$(this).removeClass(theClass);
			});
		});
	}
	
	var lateInitFadeElements = function(){
		configs.animateClasses.forEach(function(theClass){
			$("."+ theClass + configs.animateOffSuffix).each(function(){
				$(this).addClass(configs.animateTransitionClass);
			});
		});
		
		scrollSpy();
	}
	
	return {
		init: init,
	}
}(jQuery));

$(document).ready(function(){
		TechKidsApp.init();
});