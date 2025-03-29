<script setup>
import { ref } from "vue";
import axios from "axios";

const termoBusca = ref("");  // Campo de busca
const operadoras = ref([]);  // Armazena os resultados da API

const buscarOperadoras = async () => {
  try {
    const response = await axios.get(`http://localhost:8000/buscar-operadoras/`, {
      params: { termo: termoBusca.value },  // Passa o termo como parâmetro
      headers: {
        "Content-Type": "application/json",
      },
    });
    operadoras.value = response.data;  // Atualiza a lista com os dados recebidos
  } catch (error) {
    console.error("Erro ao buscar operadoras:", error);
  }
};
</script>

<template>
  <div>
    <h1>Buscar Operadoras</h1>
    <input v-model="termoBusca" placeholder="Digite um termo..." />
    <button @click="buscarOperadoras">Buscar</button>

    <table v-if="operadoras.length">
      <thead>
        <tr>
          <th>Razão Social</th>
          <th>Nome Fantasia</th>
          <th>Modalidade</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(op, index) in operadoras" :key="index">
          <td>{{ op.Razao_Social }}</td>
          <td>{{ op.Nome_Fantasia }}</td>
          <td>{{ op.Modalidade }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
input {
  margin-right: 10px;
  padding: 5px;
}

table {
  margin-top: 20px;
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid black;
  padding: 8px;
  text-align: left;
}
</style>
