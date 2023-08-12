// Import necessary scripts
import './limo_tracking.js';
import './lead_capture.js';

// DOM Elements
const limoList = document.getElementById('limo-list');
const limoDetail = document.getElementById('limo-detail');
const leadCaptureForm = document.getElementById('lead-capture-form');
const trackingMap = document.getElementById('tracking-map');

// Fetch data and update UI
async function main() {
    const limoData = await getLimoData();
    const leadData = await getLeadData();
    const trackingData = await getTrackingData();

    updateLimoList(limoData, limoList);
    updateLimoDetail(limoData, limoDetail);
    submitLeadCaptureForm(leadData, leadCaptureForm);
    updateTrackingMap(trackingData, trackingMap);
}

// Execute main function
main();