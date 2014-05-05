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
		var hh = $(this).text().trim();
        var hh1 = hh.substring(0,hh.length-1)
        var hh2 = "<a href='#comment-"+hh1+"'>@"+hh1+"楼</a>"
		var html = "<a class=\"self-comment-cancelreply\" title=\"取消回复\">"+hh+"取消回复</a>";
		$("#postcomment").find(".self-comment-title").append(html)
        $("#id_comment").val(hh2).css("height","150px");
	});

    $(document).on("click",".self-comment-cancelreply",function(){
        $(this).html("")
    })

    $(window).scroll(function(){
		if($(window).scrollTop()>400){
			$(".self-return").css("display","block");
		}
		else{
			$(".self-return").css("display","none");
		}
	});

	$(".self-return").click(function(){
		$("body,html").animate({scrollTop:0},400);
	});

    $(document).on("click",".self-comment-showstyle",function(){
        $hh = $(this).html();
        if($hh =="更多"){
            $(this).parent().css({"overflowY":"visible","maxHeight":"3000px"})
            $(this).html("收起")
        }else
        {
            $(this).parent().css({"overflowY":"hidden","maxHeight":"400px"})
            $(this).html("更多")
        }
    })

})