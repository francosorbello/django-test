<template>
  <div>
    <h1>Añadir user</h1>
    <AddUser @add-user="addUser"/>
    <h1>Usuarios</h1>
    <UserListVue @delete-user="deleteUser" :users="users"/>
  </div>
</template>

<script>
import UserListVue from './components/UserList.vue'
import AddUser from './components/AddUser.vue'

export default {
  name: 'App',
  components: {
    UserListVue,
    AddUser
  },
  data() {
    return {
      users: []
    }
  },
  methods: {
    async getUsers() {
      const res = await fetch('http://localhost:8000/api/user-api/',{
          method: 'GET',
          headers: new Headers({ 'Content-type': 'application/json'}),
      })
      this.users = await res.json()
    },
    async addUser(user) {
      const res = await fetch('http://localhost:8000/api/user-api/',{
          method: 'POST',
          headers: new Headers({ 'Content-type': 'application/json'}),
          body: JSON.stringify(user),
      })
      this.getUsers()
    },
    async deleteUser(user){
      const addr = 'http://localhost:8000/api/user-api/'+user.id+"/"
      const res = await fetch(addr,{
          method: 'DELETE',
          headers: new Headers({ 'Content-type': 'application/json'}),
          body: JSON.stringify(user),
      })
      this.getUsers()
    }
  },
  async created() {
    await this.getUsers()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
