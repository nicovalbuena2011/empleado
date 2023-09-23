

document.addEventListener('DOMContentLoaded', function () {

    const createMap = () => {
        let map = L.map('map').setView([4.739406, -74.039580], 15);
        var marker = L.marker([4.739406, -74.039580]).addTo(map);
    
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        
    
        return map
    
    }


    let map = createMap();
});

