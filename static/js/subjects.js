
let addSubjectButton = document.querySelector('#open-modal'),
    addSubjectModal = document.querySelector('#add-subject-modal'),
    closeSubjectModal = document.querySelector('#close')


addSubjectButton.addEventListener('click', () => {
    addSubjectModal.classList.add('showAnim')
    addSubjectModal.classList.remove('d-none')

})
closeSubjectModal.addEventListener('click', ()=>{
    addSubjectModal.classList.remove('showAnim')
    addSubjectModal.classList.add('d-none')

})


// update

let updateSubjectModal = document.querySelector('#update-subject-modal'),
    closeUpdateModal =  document.querySelector('#close-update-modal')
    
    closeUpdateModal.addEventListener('click', ()=>{
    updateSubjectModal.classList.remove('showAnim')
    updateSubjectModal.classList.add('d-none')
})


function openEditSubjectModal(data) {
    
    document.querySelector('#id-input').value = data['id']
    document.querySelector('#update-subject-name').value = data['name']


    updateSubjectModal.classList.add('showAnim')
    updateSubjectModal.classList.remove('d-none')

}


// delete


let close_delete_model = document.querySelector('#close-delete-model'),
    close_delete_model2 = document.querySelector('#back-button'),
    delete_modal = document.querySelector('#delete-modal')

close_delete_model.addEventListener('click', function() {
    delete_modal.classList.remove('showAnim')
    delete_modal.classList.add('d-none')
})


close_delete_model2.addEventListener('click', function() {
    delete_modal.classList.remove('showAnim')
    delete_modal.classList.add('d-none')
})

function openDeleteModal(data) {
    delete_modal.classList.remove('d-none')
    delete_modal.classList.add('showAnim')
    
    document.getElementById('fn-delete').textContent=data['name']

    document.getElementById('url').href = `${window.location.origin}/delete-subject/?id=${data['id']}`
}





