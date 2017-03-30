$(".extend").click(function() {
	$('.hiddenSound[data-category="' + $(this).attr("data-category") + '"]').toggle();
})

$('.button').click(function() {
	var sound = $(this).attr("data-sound");
	if (sound != undefined) {
		$("[data-soundPlayer='" + sound + "']")[0].pause();
		$("[data-soundPlayer='" + sound + "']")[0].currentTime = 0;
		$("[data-soundPlayer='" + sound + "']")[0].play();
	}
})