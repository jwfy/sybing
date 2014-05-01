$(document).ready(function(){

	/*
	$(".sidebar-item-display").hover(function(){
		$(this).parent().nextAll().slideDown()
		$(this).html("收缩");
		console.log("收缩")
	},function(){
		$(this).parent().nextAll().slideUp()
		$(this).html("展开");	
		console.log("展开")
	})
	
	*/
	
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
	})
    $(".self-comment-showstyle").click(function(){
		$(this).html("hehe")
	})
})