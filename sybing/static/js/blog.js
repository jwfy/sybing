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
	
	$(".self-comment-number").click(function(){
		$(".self-comment-cancelreply").detach();
		var hh = $(this).text();
		var html = "<a class=\"self-comment-cancelreply\" title=\"取消回复\">"+hh+"取消回复</a>";
		$("#postcomment").find(".self-comment-title").append(html)
		$("#id_comment").html(hh);
	});
	
    $(".self-comment-cancelreply").live("click",function(){
		alert("hhe");
	})
	
})