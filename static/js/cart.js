(function($) {
	
	var isClosed = true;
	$('a.viewcart').click(function(){
	if(isClosed)
	{
		$(this).addClass("active");
		$(this).removeClass("hover");
		$('form#myForm').slideDown('normal');
		isClosed = false;
	}
	else
	{
		$(this).removeClass("active");
		$('form#myForm').slideUp('normal');
		isClosed = true;
	}
	});
	
	$("a.plus"+1).click(function(){
	$(this).parents(".num").val()+=1;
	});
	$(".pane .delete").click(function(){
		$(this).parents(".pane").animate({ opacity: 'hide' }, "slow");
	});
})(jQuery);


