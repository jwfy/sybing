$(document).ready(function(){

	
	$(".self-list-commit").hover(
	function(){
		$(this).css("border","2px solid #428BCA")
		var height = $(this).height();
		if(parseInt(height)>=420){
			$(this).find(".self-comment-contain").prepend("<div class=\"self-comment-showstyle\">更多</div>");
		}
	},function(){
		$(this).removeAttr('style');
		var height = $(this).height();
		if(parseInt(height)>=420)
			$(this).find(".self-comment-showstyle").detach();
	});
	
})