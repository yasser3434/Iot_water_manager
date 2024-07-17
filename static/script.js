function updateQualityBox(quality) {
    // Reset all boxes
    document.getElementById('good-box').style.display = 'none';
    document.getElementById('error-box').style.display = 'none';
    document.getElementById('fair-box').style.display = 'none';
    document.getElementById('poor-box').style.display = 'none';

    // Display the appropriate box
    if (quality === 'Good' || quality === 'Excellent for drinking') {
        document.getElementById('good-box').style.display = 'block';
        document.getElementById('good-box').textContent = quality;  // Text inside the box
    } else if (quality === 'ERROR no contact with water') {
        document.getElementById('error-box').style.display = 'block';
    } else if (quality === 'Fair') {
        document.getElementById('fair-box').style.display = 'block';
    } else if (quality === 'Poor not good for drinking') {
        document.getElementById('poor-box').style.display = 'block';
    }
}

setInterval(function(){
    var img = document.getElementById('plot');
    img.src = '/plot.png?' + new Date().getTime();

    // Fetch the latest quality data
    fetch('/latest-quality')
        .then(response => response.text())
        .then(quality => updateQualityBox(quality));
}, 1000); // Refresh every 1000 milliseconds (1 second)
